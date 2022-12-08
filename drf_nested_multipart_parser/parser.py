from typing import Any

from rest_framework import parsers


class NestedMultipartParser(parsers.MultiPartParser):
    def decode(self, key: str, value: Any, data: dict[str, Any]) -> None:
        def has_grandchild(key):
            return '][' in key

        def has_child(key):
            return '[' in key and ']' in key

        def insert_value(key: dict | list, child_key: str, value: Any) -> None:
            if isinstance(key, list):
                key.append(value)
            else:
                key[child_key] = value

        if not has_child(key):
            return insert_value(data, key, value)

        index_left_bracket = key.index('[')
        index_right_bracket = key.index(']')

        parent_key = key[:index_left_bracket]
        child_key = key[index_left_bracket + 1:index_right_bracket]

        if parent_key not in data:
            data[parent_key] = {} if len(child_key) > 0 else []

        if not has_grandchild(key):
            return insert_value(data[parent_key], child_key, value)

        grandchild_key = child_key + key[index_right_bracket + 1:]  # parent[child][grandchild] > child[grandchild]
        self.decode(key=grandchild_key, value=value, data=data[parent_key])

    def transform_dicts_with_numeric_keys_into_lists(self, data: dict[str, Any]):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = self.transform_dicts_with_numeric_keys_into_lists(value)

        if all(key.isnumeric() for key in data):
            return [value for value in data.values()]
        return data

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(stream, media_type, parser_context)

        data = {}
        for dictionary in (result.data, result.files):
            for key, value in dictionary.items():
                self.decode(key=key, value=value, data=data)

        return self.transform_dicts_with_numeric_keys_into_lists(data)

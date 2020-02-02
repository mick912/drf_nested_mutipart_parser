from rest_framework import parsers


class NestedMultipartParser(parsers.MultiPartParser):

    def decode(self, key, value, data):

        if '[' in key and ']' in key:

            index_left_bracket = key.index('[')
            index_right_bracket = key.index(']')

            parent_key = key[:index_left_bracket]
            child_key = key[index_left_bracket + 1:index_right_bracket]

            if parent_key not in data:
                data[parent_key] = {} if len(child_key) > 0 else []

            if '][' in key:  # if has child
                key = child_key + key[index_right_bracket + 1:]  # root[parent][child] > parent[name3]
                self.decode(key=key, value=value, data=data[parent_key])
            elif isinstance(data[parent_key], list):
                data[parent_key].append(value)
            else:
                data[parent_key][child_key] = value

        else:
            data[key] = value

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(stream=stream, media_type=media_type, parser_context=parser_context)
        data = {}
        for key, value in result.data.items():
            self.decode(key=key, value=value, data=data)

        return parsers.DataAndFiles(data, result.files)

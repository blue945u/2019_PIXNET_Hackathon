import sys
import json
import io

input_file_name=sys.argv[1]
output_file_name=sys.argv[2]
key_word=sys.argv[3]

with io.open( input_file_name , 'r') as in_file, io.open( output_file_name , 'w') as out_file:
    for line in in_file:
        dic = json.loads(line)
        # print(dic['keyword_top10'])
        keyword_list = []
        if dic.__contains__('keyword_top10'):
            for keyword in dic['keyword_top10']:
                if keyword.__contains__('word'):
                    keyword_list.append(keyword['word'])
            if key_word in keyword_list:
                if dic.__contains__('content'):
                    dic.pop('content', None)
                if dic.__contains__('image_links'):
                    dic.pop('image_links', None)
                # if dic.__contains__('title'):
                    # print(dic['title'])
                out_file.write(json.dumps(dic, ensure_ascii=False))

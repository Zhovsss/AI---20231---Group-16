import os

for type in ['train', 'test']:
    path = type + '/labels'
    files = os.listdir(path)
    for file in files:
        new_label = []
        with open(path + '/' + file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                temp_list = line.replace('\n', '').strip().split(' ')
                if temp_list[0] == '3':
                    temp_list[0] = '1'
                    new_label.append(' '.join(temp_list))
                else:
                    new_label.append(' '.join(temp_list))
        with open(path + '/' + file, 'w') as f:
            new_label_content = ''
            if len(new_label) > 0:
                for line in new_label[:-1]:
                    new_label_content += line + '\n'
                new_label_content += new_label[-1]
                f.write(new_label_content)
            else:
                f.write('')



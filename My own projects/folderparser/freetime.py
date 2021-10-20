from json import load

LIST_OF_FILES = []


class FolderFounder:
    """
    Сьют для рекурсивного парсинга уровней папок
    """

    def __init__(self, main_flow: dict):
        self.main_flow = main_flow
        self.folders = [self.main_flow['name']]

    def flow_parsing(self, flow: dict):

        self.folders.append(flow['name'])
        flow_files = flow['files']
        flow_sub_folders = flow['sub_folders']

        if len(flow_sub_folders) > 0:
            for sub_folder in flow_sub_folders:
                self.flow_parsing(sub_folder)
        if len(flow_files) > 0:
            for file in flow_files:
                LIST_OF_FILES.append({f'File name is {file}': f'Its directory is {self.folders}'})
        self.folders.pop()


if __name__ == '__main__':
    with open('folders.json') as fhand:
        data = load(fhand)

    for main_flow in data:
        founder = FolderFounder(main_flow)
        for flow in main_flow["sub_folders"]:
            print(flow)
            founder.flow_parsing(flow)
    for ls in LIST_OF_FILES:
        print(ls)

import sys,json,requests
class gituser:
    def __init__(self,userid):
        self.userid=userid
        self._repo=dict()
        self._url='https://api.github.com/users/' + self.userid + '/repos'
        self.get_repo()
    
    def get_repo(self):
        time=json.loads(requests.get(self._url).text)
        for i in time:
            try:
                self._repo.setdefault(i['name'],0)
                url = "https://api.github.com/repos/" + self.userid + "/" + i["name"] + "/commits"
                self._repo[i['name']]=len(json.loads(requests.get(url).text))
            except Exception as e:
                print(e)
                sys.exit()

    def get_repo_list(self):
        return self._repo.keys()
    
    def get_commits(self,name:str):
        if name in self._repo.keys():
            return self._repo[name]
        else:
            return -1

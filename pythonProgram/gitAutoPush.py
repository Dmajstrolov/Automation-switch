from git import Repo

PATH_OF_GIT_REPO = r'C:\Users\HK\Documents\Examensarbete\switchbackup.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo('https://github.com/Dmajstrolov/PythonScripts.git')
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()
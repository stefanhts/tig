import sys, getopt
from datetime import date

# tig will take arguments from the command line. 
# The format should look something like:
# tig get dirname > this will pull the newest version of dir from the server
# tig create > this will mark the directory as a valid tig project
# tig push name > this will push changes to the dir to the server with the given name
# possibly implement tig pull specific > this will pull specific version

CREATE = 'create'
GET = 'get'
PUSH = 'push'
TEMP_LOC = '~/Documents/Projects/Temp/'
AUTHOR = 'stefanhts'
DATE = date.today() 
CHANGESET = 'init'

def create():
    try:
        f = open(".tig", "x")
        f.close()
        f = open(".tig", "w")
        f.write(f"CHANGESET={CHANGESET}")
        f.write(f"DATE={DATE}")
        f.write(f"AUTHOR={AUTHOR}")
        f.close()

    except:
        print 'Directory is already tig ready'

def push(dirname):
    print('changeset with name: '+dirname+' has been pushed')

def get(projname):
    print('project: ' +projname+' has been fetched')

def main(argv):
    _, args = getopt.getopt(argv, "", "")

    if args[0] == CREATE:
        if len(args) > 1:
            CHANGESET = args[1]
        create()
    elif args[0] == GET:
        get(args[1])
    elif args[0] == PUSH:
        push(args[1])

if __name__ == '__main__':
    main(sys.argv[1:])




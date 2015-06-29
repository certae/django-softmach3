import os



def ReadFile(inFile, mode='r'):
    contents = ""
    try:
        f=open(inFile, mode)
        contents = f.read()
        f.close()
    except:
        pass
    return contents


def WriteFile(inFile, contents, mode = 'w'):
    f=open(inFile, mode)
    f.write(contents)
    f.close()



def verifyDirPath( pathName ):
    """
    Asegura q el directorio de base exista 
    """

    try: 
        if os.path.exists(pathName):
            return os.path.isdir( pathName )    
        
        os.makedirs(pathName)    
        return True 
    except: 
        return False 


def joinPath( *args ):
    """
    Asegura q el directorio de base exista 
    """

    return os.path.join( args )



# print os.path.split(fp)
# # ('/home/aa/bb', 'ff.html')

# print os.path.dirname(fp)
# # /home/aa/bb

# print os.path.basename(fp)
# # ff.html

# print os.path.splitext("/home/aa/bb/ff.html")[1]
# # '.html'



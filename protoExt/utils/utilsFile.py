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
    Retorna el path exapandido o falso en caso de error 
    """

    pathName = os.path.expanduser(pathName)
    
    try: 
        if os.path.exists(pathName):
            if not os.path.isdir( pathName ):return False
            return pathName 
        
        os.makedirs(pathName)    
        return pathName 
    except: 
        return False 


def joinPath( *args ):
    """
    Asegura q el directorio de base exista 
    """

    return os.path.join( *args )



# print os.path.split(fp)
# # ('/home/aa/bb', 'ff.html')

# print os.path.dirname(fp)
# # /home/aa/bb

# print os.path.basename(fp)
# # ff.html

# print os.path.splitext("/home/aa/bb/ff.html")[1]
# # '.html'



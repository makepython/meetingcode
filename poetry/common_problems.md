On macOs, the certificates for SSL may not be installed.

    $ poetry search click
                                                                                                                    
    [SSLCertVerificationError]                                                                           
    [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)  
                                                                                                                    

    $ sudo /Applications/Python\ 3.7/Install\ Certificates.command 
    Password:
     -- pip install --upgrade certifi
    The directory '/Users/sbo/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
    The directory '/Users/sbo/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
    Collecting certifi
      Downloading https://files.pythonhosted.org/packages/69/1b/b853c7a9d4f6a6d00749e94eb6f3a041e342a885b87340b79c1ef73e3a78/certifi-2019.6.16-py2.py3-none-any.whl (157kB)
        100% |████████████████████████████████| 163kB 3.4MB/s 
    Installing collected packages: certifi
      Found existing installation: certifi 2018.11.29
        Uninstalling certifi-2018.11.29:
          Successfully uninstalled certifi-2018.11.29
    Successfully installed certifi-2019.6.16
    You are using pip version 19.0.3, however version 19.2.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
     -- removing any existing file or link
     -- creating symlink to certifi certificate bundle
     -- setting permissions
     -- update complete

    $ /Applications/Python\ 3.7/Update\ Shell\ Profile.command 
    This script will update your shell profile when the 'bin' directory
    of python is not early enough of the PATH of your shell.
    These changes will be effective only in shell windows that you open
    after running this script.
    All right, you're a python lover already

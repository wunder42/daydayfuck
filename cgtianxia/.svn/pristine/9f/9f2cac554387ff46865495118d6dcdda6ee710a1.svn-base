#coding=utf8

from django.core.files.storage import FileSystemStorage
import os 

class ImageStorage(FileSystemStorage):
    from django.conf import settings
    
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(ImageStorage, self).__init__(location, base_url)
        
    def _save(self, name, content):
        full_path = self.path(name)

        # Create any intermediate directories that do not exist.
        # Note that there is a race between os.path.exists and os.makedirs:
        # if os.makedirs fails with EEXIST, the directory was created
        # concurrently, and we can continue normally. Refs #16082.
        directory = os.path.dirname(full_path)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError, e:
                if e.errno != errno.EEXIST:
                    raise
        if not os.path.isdir(directory):
            raise IOError("%s exists and is not a directory." % directory)

        # There's a potential race condition between get_available_name and
        # saving the file; it's possible that two threads might return the
        # same name, at which point all sorts of fun happens. So we need to
        # try to create the file, but if it already exists we have to go back
        # to get_available_name() and try again.

        # while True:
        #     try:
        #         # This file has a file path that we can move.
        #         if hasattr(content, 'temporary_file_path'):
        #             file_move_safe(content.temporary_file_path(), full_path)
        #             content.close()

        #         # This is a normal uploadedfile that we can stream.
        #         else:
        #             # This fun binary flag incantation makes os.open throw an
        #             # OSError if the file already exists before we open it.
        #             fd = os.open(full_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_BINARY', 0))
        #             try:
        #                 locks.lock(fd, locks.LOCK_EX)
        #                 for chunk in content.chunks():
        #                     os.write(fd, chunk)
        #             finally:
        #                 locks.unlock(fd)
        #                 os.close(fd)
        #     except OSError, e:
        #         if e.errno == errno.EEXIST:
        #             # Ooops, the file exists. We need a new file name.
        #             name = self.get_available_name(name)
        #             full_path = self.path(name)
        #         else:
        #             raise
        #     else:
        #         # OK, the file save worked. Break out of the loop.
        #         break

        # if settings.FILE_UPLOAD_PERMISSIONS is not None:
        #     os.chmod(full_path, settings.FILE_UPLOAD_PERMISSIONS)

        from os import environ  
        online = environ.get("APP_NAME", "")   
      
        if online:  
            import sae.const  
            access_key = sae.const.ACCESS_KEY  
            secret_key = sae.const.SECRET_KEY  
            appname = sae.const.APP_NAME  
            domain_name = "upload"         
            prefix = name.split('/')[-2] 
            import sae.storage      
            s = sae.storage.Client()  
            ob = sae.storage.Object(content.read())  
            url = s.put(domain_name, prefix+'/'+content.name, ob)  
        return os.path.split(name)[1]


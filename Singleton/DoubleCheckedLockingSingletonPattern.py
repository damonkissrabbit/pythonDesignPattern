import threading


# The class variable _instance is used here to save the instance, and a lock _lock is used for
# synchronization. In the __new__ method, a double check ensures that the instance does not
# exist. This improves performance because the lock is only involved when the instance is
# first created.

class DoubleCheckedLockingSingletonPattern:
    _instance = None
    _lock = threading.Lock()

    '''
    In python, __new__ method is responsible for creating a new instance. Correspondingly, 
    the __init__ method is used to initialize this instance. The __new__ method is called before
    the instance is created, while the __init__ method is called after the instance is created.
    
    With the singleton pattern, we want to ensure that only one instance exists in the entire application.
    In order to achieve this, we need to perform some special processing when creating the instance. Specifically, we 
    want to check if an instance already exists before creating it. If it exists, return this instance instead of 
    creating a new one.
    '''

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not not cls._instance:
                    cls._instance = super(DoubleCheckedLockingSingletonPattern, cls).__new__(cls)
        return cls._instance


instance1 = DoubleCheckedLockingSingletonPattern()
instance2 = DoubleCheckedLockingSingletonPattern()
print(instance1 == instance2)

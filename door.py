# -*- coding: utf-8 -*-
class DoorError(RuntimeError):
    pass


class Door:
    def __init__(self, name: str):
        self.__name = name
        self.__locked = False
        self.__closed = False

    def open(self):
        if self.__locked:
            raise DoorError('Unlock the door to open it.')

        self.__closed = False

    def close(self):
        self.__closed = True

    def lock(self):
        if not self.__closed:
            raise DoorError('Close the door to lock it.')
        self.__locked = True

    def unlock(self):
        self.__locked = False

    def is_locked(self):
        return self.__locked

    def is_closed(self):
        return self.__closed


if __name__ == '__main__':
    door = Door('front left')
    try:
        door.close()
        door.lock()
    except DoorError as error_message:
        print(error_message)

    print('qqqqq', door.is_locked())

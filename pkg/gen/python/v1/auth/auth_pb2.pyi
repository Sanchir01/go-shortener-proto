from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNSPECIFIED: _ClassVar[Role]
    ADMIN: _ClassVar[Role]
    USER: _ClassVar[Role]
ROLE_UNSPECIFIED: Role
ADMIN: Role
USER: Role

class RegisterRequest(_message.Message):
    __slots__ = ("phone", "email", "password", "title")
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    phone: str
    email: str
    password: str
    title: str
    def __init__(self, phone: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: str
    def __init__(self, ok: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("email", "phone", "title", "role")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    email: str
    phone: str
    title: str
    role: Role
    def __init__(self, email: _Optional[str] = ..., phone: _Optional[str] = ..., title: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ...) -> None: ...

class ConfirmRegisterRequest(_message.Message):
    __slots__ = ("phone", "email", "password", "title", "code")
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    phone: str
    email: str
    password: str
    title: str
    code: str
    def __init__(self, phone: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., title: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class ConfirmRegisterResponse(_message.Message):
    __slots__ = ("email", "phone", "title", "role")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    email: str
    phone: str
    title: str
    role: Role
    def __init__(self, email: _Optional[str] = ..., phone: _Optional[str] = ..., title: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ...) -> None: ...

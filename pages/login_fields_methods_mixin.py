# Static typing version

# https://andrewbrookins.com/technology/building-implicit-interfaces-in-python-with-protocol-classes/
# https://mypy.readthedocs.io/en/latest/more_types.html#mixin-classes
# https://stackoverflow.com/questions/51930339/how-do-i-correctly-add-type-hints-to-mixin-classes

#
# class HasLoginFields(Protocol):
#     @property
#     def username(self) -> TextBox: ...
#
#     @property
#     def password(self) -> PasswordTextBox: ...
#
#     @property
#     def show_password_checkbox(self) -> CheckBox: ...


# class LoginFieldsMethodsMixin:
#
#     def enter_username(self: HasLoginFields, username):
#         self.username.enter_text(username)
#
#     def enter_password(self: HasLoginFields, password):
#         self.password.enter_text(password)
#
#     def toggle_show_password(self: HasLoginFields):
#         self.show_password_checkbox.toggle()
#
#     def is_password_masked(self: HasLoginFields):
#         return self.password.is_type_password()

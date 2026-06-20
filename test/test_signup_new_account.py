import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_lowercase
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])



import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_signup_new_account(app):
    username = random_string("user_", 10)
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exists(username=username, password=password)
    app.signup.new_user(username, email, password)
    #app.session.login(username, password)
    #assert app.session.is_logged_in_as(username)
    #app.session.logout()
    assert app.soap.can_login(username, password)

def test_signup_new_account(app):
    username = random_string("user_", 10)
    email = username + "@localhost"
    password = "password"

    print("STEP 1. Generated user:")
    print("username:", username)
    print("email:", email)
    print("password:", password)

    print("STEP 2. Create mailbox in James")
    app.james.ensure_user_exists(username=username, password=password)

    print("STEP 3. Register user in Mantis and set password")
    app.signup.new_user(username, email, password)

   # print("STEP 4. Check login via SOAP")
   # assert app.soap.can_login(username, password)

    #print("STEP 5. Login via UI")
    #app.session.login(username, password)

    #print("STEP 6. Check logged user")
   # assert app.session.is_logged_in_as(username)
    print("STEP 4. Login via UI")
    app.session.login(username, password)

    print("STEP 5. Check logged user")
    assert app.session.is_logged_in_as(username)

    print("STEP 6. Logout")
    app.session.logout()
    #print("STEP 7. Logout")
    #app.session.logout()

import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_lowercase
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


def test_signup_new_account(app):
    username = random_string("user_", 10)
    email = username + "@localhost"
    password = "password"

    print("STEP 1. Generated user:")
    print("username:", username)
    print("email:", email)
    print("password:", password)

    print("STEP 2. Create mailbox in James")
    app.james.ensure_user_exists(username=username, password=password)

    print("STEP 3. Register user in Mantis and set password")
    app.signup.new_user(username, email, password)

    print("STEP 4. Check user is already logged in")
    assert app.session.is_logged_in_as(username)

    print("STEP 5. Logout")
    app.session.logout()


#def test_signup_new_account(app):
#    assert app.soap.can_login("administrator", "root")
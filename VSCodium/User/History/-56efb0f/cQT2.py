from numb3rs import validate

def test_the_format():
    # Return False
    assert validate("cat") == False
    assert validate("1 2 3 4") == False
    assert validate("1.2.sad") == False
    assert validate("safsaf1.2.3.4") == False
    assert validate("1.2saf.342.21432") == False

    # Return True
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True

def test_the_ip():
    # Return False
    ## Possible casses:
    ### 1- One of the numbers is bigger than  
from numb3rs import validate

def test_the_format():
    # Return False
    assert validate("cat") == False
    assert validate("1 2 3 4") == False
    assert validate("1.2.sad") == False
    assert validate("safsaf1.2.3.4") == False
    assert validate("1.2saf.342.21432") == False
    assert validate("1.1") == False
    assert validate("1.1.1.1.1.1.1") == False

    # Return True
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True

def test_the_ip():
    # Return False
    ## Possible casses:
    ### 1- One of the numbers is bigger than 255 
    assert validate("300.1.1.1") == False
    assert validate("1.300.1.1") == False
    assert validate("1.1.300.1") == False
    assert validate("1.1.1.300") == False
    ### 2- One of the numbers has zeros in the left
    assert validate("001.1.1.1") == False
    assert validate("1.001.1.1") == False
    assert validate("1.1.001.1") == False
    assert validate("1.1.1.001") == False
    ### 3- One of the numbers is negative
    assert validate("001.1.1.1") == False
    assert validate("1.001.1.1") == False
    assert validate("1.1.001.1") == False
    assert validate("1.1.1.001") == False
 
    
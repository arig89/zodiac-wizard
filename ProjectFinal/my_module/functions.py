"""A collection of functions for doing my project."""

#Function for finding zodiac sign.
def zodiac_function(user_month, user_day):
    """ Using conditionals, compares numbers of months and days to determine sign.   
    
        Parameters
        ----------
        user_month : int
            The number of the month user was born in, determines sign. 
        user_day: int 
            The day the user was born on, compared using comparison operators
            to determine sign.     
    
        Returns
        -------
        sign : str
            The determined sign after comparison. """
     
#Leo    
    if user_month == 8 and user_day <= 23:
        sign = "Leo"
        return sign
    elif user_month == 8 and user_day > 23:
        sign = "Virgo"
        return sign
#Virgo
    if user_month == 9 and user_day <= 22:
        sign = "Virgo"
        return sign
    elif user_month == 9 and user_day > 22:
        sign = "Libra"
        return sign
#Libra
    if user_month == 10 and user_day <= 22:
        sign = "Libra"
        return sign
    elif user_month == 10 and user_day > 22:
        sign = "Scorpio"
        return sign
#Scorpio
    if user_month == 11 and user_day <= 23:
        sign = "Scorpio"
        return sign
    elif  user_month == 11 and user_day > 23:
        sign = "Sagittarius"
        return sign
#Sagittarius
    if user_month == 12 and user_day <= 21:
        sign = "Sagittarius"
        return sign
    elif  user_month == 12 and user_day > 21:
        sign = "Capricorn"
        return sign
#Capricorn
    if user_month == 12 and user_day <= 21:
        sign = "Sagittarius"
        return sign
    elif  user_month == 12 and user_day > 21:
        sign = "Capricorn"
        return sign
#Aquarius
    if user_month == 1 and user_day <= 19:
        sign = "Capricorn"
        return sign
    elif  user_month == 1 and user_day > 19:
        sign = "Aquarius"
        return sign
#Pisces
    if user_month == 2 and user_day <= 18:
        sign = "Aquarius"
        return sign
    elif user_month == 2 and user_day > 18:
        sign = "Pisces"
        return sign
#Aries
    if user_month == 3 and user_day <= 20:
        sign = "Pisces"
        return sign
    elif  user_month == 3 and user_day > 20:
        sign = "Aries"
        return sign
#Taurus
    if user_month == 4 and user_day <= 20:
        sign = "Aries"
        return sign
    elif  user_month == 4 and user_day > 20:
        sign = "Taurus"
        return sign
#Gemini
    if user_month == 5 and user_day <= 20:
        sign = "Taurus"
        return sign
    elif  user_month == 5 and user_day > 21:
        sign = "Gemini"
        return sign
#Cancer
    if user_month == 6 and user_day <= 20:
        sign = "Gemini"
        return sign
    elif  user_month == 6 and user_day > 20:
        sign = "Cancer"
        return sign
    elif user_month == 7 and user_day <= 22:
        sign = "Cancer"
        return sign
    
    
    
    
#Function for finding zodiac horoscope.
def zodiac_horoscope(user_sign):
    """ Using conditionals, assigns a certain horoscope to be returned based on user's sign.   
    
        Parameters
        ----------
        user_sign : str
            The user's zodiac sign as determined by their birthday.      
        
        Returns
        -------
        output : str
            Prints a string corresponding to user's sign. """
    
    if user_sign == "Aquarius" :
        output = "you will meet many new friends!"
        return output
    elif user_sign == "Pisces":
        output = "you will find a new hobby!"
        return output
    elif user_sign == "Aries":
        output = "your love life will be exciting!"
        return output
    elif user_sign == "Taurus":
        output = "you will receive an unexpected gift."
        return output
    elif user_sign == "Gemini":
        output = "you will run into an old friend."
        return output
    elif user_sign == "Cancer":
        output = "you will grow closer to your family."
        return output
    elif user_sign == "Leo":
        output = "you will try something you've never done before."
        return output
    elif user_sign == "Virgo":
        output = "you will let loose and have fun!"
        return output
    elif user_sign == "Libra":
        output = "you will get more serious about an upcoming project."
        return output
    elif user_sign == "Scorpio":
        output = "you will have a lot of creative energy!"
        return output
    elif user_sign == "Sagittarius":
        output = "you will throw a lot of parties!"
        return output
    elif user_sign == "Capricorn":
        output = "you will find success in your career!"
        return output
    
    


#Function for finding compatibility between user and friend.
def zodiac_compatibility(user_sign, friend_sign):
    """ Using comparison operators and conditionals, returns a given compatibility message.  
    
        Parameters
        ----------
        user_sign : str
            The user's zodiac sign as determined by their birthday input.      
        friend_sign : str
            The friend's zodiac sign as determined by their birthday input.
        Returns
        -------
        message : str
            Prints a string about friendship compatibility, changing depending on 
            whether the friends have the same signs or not."""
    
    if user_sign == friend_sign:
        message = "The stars say: you are best friends!"
        return message
    elif user_sign != friend_sign:
        message = "You get along quite well!"
        return message


    


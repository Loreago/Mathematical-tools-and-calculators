# note frequency calculator
def octave(o):
    base_frequency=(55*(2**(o-1)))
    return base_frequency

def note(f):
    if f == "C":
        f=-9
        return f
    elif f== "C#" or f == "Db":
        f=-8
        return f
    elif f== "D":
        f=-7
        return f
    elif f== "D#" or f == "Eb":
        f=-6
        return f
    elif f== "E":
        f=-5
        return f
    elif f== "F":
        f=-4
        return f
    elif f== "F#" or f == "Gb":
        f=-3
        return f
    elif f== "G":
        f=-2
        return f
    elif f== "G#" or f == "Ab":
        f=-1
        return f
    elif f== "A":
        f= 0
        return f
    elif f== "A#" or f == "Bb":
        f= 1
        return f
    elif f== "B":
        f= 2
        return f
    
def frequency(unote, oct):
    k=note(unote)
    Aa=octave(oct)
    final_frequency=Aa*((2**(1/12))**k)
    return final_frequency
  


if __name__ == "__main__":
    print("Hello!")
    print("This program calculates the frequency of a given piano note.")
    user_octave=int(input("Please enter the octave of your note: "))
    user_note=input("Please enter your note in capital letters eg: C, D# or Db: ")
    user_frequency=frequency(user_note, user_octave)
    print(f"Your note {user_note}{user_octave} has a frequency of {user_frequency:.2f} hz")
    print("Thank you!")

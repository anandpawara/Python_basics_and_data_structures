def check(string, sub_str):
    if(string.find(sub_str)== -1):
        print("String not found")
    else:
        print("String found")

string = 'geeks for geeks'
sub_str = 'ges'
check(string,sub_str)
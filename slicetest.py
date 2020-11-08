s = "slicing test, phone number : 0123456789";
l = len(s);
print(s[14: l]);

#reverse using slicing
print(s[::-1]);

#slicing using steps
print(s[0:l:2]);
print(s[::2]);

my_string = "I love programming in Python more than Ruby or Perl";
print(my_string[-12])
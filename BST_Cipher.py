#  File: BST_Cipher.py

#  Description: This program encrypts and decrypts strings using a binary search tree 

#  Created by: Alex Liddle

#  Date Created: 4/18/2018

#  Date Last Modified: 4/20/2018

class Node (object):
  # Constructor
  def __init__(self, data):
    self.data = data
    self.lchild = None
    self.rchild = None
   
  # String representation  
  def __str__(self):
    return str(self.data)

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None
    keyList = []
    for key in encrypt_str:
      if (key not in keyList):
        keyList.append(key)
    for key in keyList:
      self.insert(key)

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    newNode = Node(ch)
    if (self.root == None):
      self.root = newNode
      return
    current = self.root
    parent = self.root
    while (current != None):
      parent = current
      if (ch < current.data):
        current = current.lchild
      else:
        current = current.rchild
    if (ch < parent.data):
      parent.lchild = newNode
    else:
      parent.rchild = newNode

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    if (ch == self.root.data):
      return '*'
    string = ''
    current = self.root
    while (current != None) and (current.data != ch):
      if (ch < current.data):
        string += '<'
        current = current.lchild
      else:
        string += '>'
        current = current.rchild
    if (current == None):
      return ''
    return string

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root
    if (st == '*'):
      return current.data
    for ch in st:
      if (ch == '<'):
        current = current.lchild
      if (ch == '>'):
        current = current.rchild
    return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    string = ''
    for ch in st:
      string += self.search(ch) + '!'
    string = string[:len(string)-1]
    return string

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    string = ''
    encrypted = st.split('!')
    for i in encrypted:
      string += self.traverse(i)
    return string

def main():

  # create cipher key
  print()
  key = str(input("Enter encryption key: "))
  print()
  cipher = Tree(key)

  # test encryption method
  to_encrypt = str(input("Enter string to be encrypted: "))
  encrypted = cipher.encrypt(to_encrypt)
  print("Encrypted string:",encrypted)

  # test decryption method
  print()
  to_decrypt = str(input("Enter string to be decrypted: "))
  decrypted = cipher.decrypt(to_decrypt)
  print("Decrypted string:",decrypted)
  print()
  
main()

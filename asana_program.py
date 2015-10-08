import json
with open("yoga_asanas_json.json") as json_data:
    data = json.load(json_data)
    print type(data)


total_practice = []
# total_practice.items()
# total_practice.keys()
# ratings.values()

integration_question1 = raw_input ("Do you want to add the Integration Series? ")

if integration_question1 == "Yes":
    #print 'YES: 4_minutes'
#elif integration_question1 == "No":
    #print "NO: zero_minutes"

    #integration_question1 = input()
    #total_practice = int(integration_question1)
    total_practice.append("Integration")


#total_practice.items()
#total_practice.keys()
#total_practice.values()

# print total_practice


# for key in total_practice: 
#     print key 




integration_question2 = raw_input ("Do you want to add the Intention Series? ")
#print integration_question2
if integration_question2 == "Yes":
    #print 'YES: 4_minutes' ADD CORRECT TIME FOR 2-13 !!!!!!!!!!!!
    total_practice.append("Intention")

 
integration_question3 = raw_input ("Do you want to add the Sun Salutation A Series? ")
#print integration_question3
if integration_question3 == "Yes":
    #print 'YES: 4_minutes' 
    total_practice.append("Sun_Salutation A")                                                                                 
 
integration_question4 = raw_input ("Do you want to add the Sun Salutation B Series? ")
#print integration_question4
if integration_question4 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Sun_Salutation B")                                                                                          

 
integration_question5 = raw_input ("Do you want to add the Core Strengthening Series? ")
#print integration_question5
if integration_question5 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Core_Strengthening_Series")                                                                                          
                                                                                         

 
integration_question6 = raw_input ("Do you want to add the Crescent Lunge Series? ")
#print integration_question6
if integration_question6 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Crescent_Lunge_Series")                                                                                           

 
integration_question7 = raw_input ("Do you want to add the Balancing Series? ")
#print integration_question7
if integration_question7 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Balancing_Series")                                                                                           
                                                                          

 
integration_question8 = raw_input ("Do you want to add the Triangle Series? ")
#print integration_question8
if integration_question8 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Triangle_Series")                                                                               

 
integration_question9 = raw_input ("Do you want to add the Hip Opener Series? ")
#print integration_question9
if integration_question9 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Hip_Opener_Series")                                                                                 

 
integration_question10 = raw_input ("Do you want to add the Spine Strengthening Series? ")
#print integration_question10
if integration_question10 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Spine_Strengthening_Series")                                                                                       

 
integration_question11 = raw_input ("Do you want to add the Forward Fold Series? ")
#print integration_question11
if integration_question11 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Forward_Fold_Series")   


integration_question12 = raw_input ("Do you want to add the Surrender Series? ")
#print integration_question12
if integration_question12 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Surrender_Series")                                                                                        

integration_question13 = raw_input ("Do you want to add Namaste? ")
#print integration_question13
if integration_question13 == "Yes":
#print 'YES: 4_minutes'
    total_practice.append("Namaste")  


print total_practice

print data
for key in total_practice:
    print data[key]




# data= []
# with open('yoga_asanas_json.json', 'r') as f:
#     for line in f:
#         data.append(json.loads(line))
    #print f.read()
    # for line in f:
    #     print json.loads(line)

#print yoga_asanas_json



# print yoga_asanas

# yoga_asanas = ["Integration", "Sun_Salutation A", "Sun Salutation B",  ]

                                                                                                                      
                                               
                                                                                    
# yoga_asanas = ["Integration", "Sun_Salutation A",   ]
# yoga_asanas = ["Integration", "Sun_Salutation A", ]
                        
                             
# integration_question1 = raw_input ("Do you want to add the Integration Series? ")

# YES = bool(1)
# FALSE = bool(0)


# total_practice = []

# integration_question1 = raw_input ("Do you want to add the Integration Series? ")

# if integration_question1 == "Yes":
#     #print 'YES: 4_minutes'

#     total_practice.append("Integration")

#     import json
# with open("yoga_asanas_json.json") as json_data:
#     read_file = json_data.read()
#     #print read_file



# data= []
# with open('yoga_asanas_json.json', 'r') as f:
#     for line in f:
#         data.append(json.loads(line))
    #print f.read()
    # for line in f:
    #     print json.loads(line)

#print yoga_asanas_json



# print yoga_asanas

# yoga_asanas = ["Integration", "Sun_Salutation A", "Sun Salutation B",  ]

                                                                                                                      
                                               
                                                                                    
# yoga_asanas = ["Integration", "Sun_Salutation A",   ]
# yoga_asanas = ["Integration", "Sun_Salutation A", ]
                        
                             
# integration_question1 = raw_input ("Do you want to add the Integration Series? ")

# YES = bool(1)
# FALSE = bool(0)


# total_practice = []
# # total_practice.items()
# # total_practice.keys()
# # ratings.values()

# integration_question1 = raw_input ("Do you want to add the Integration Series? ")

# if integration_question1 == "Yes":
#     #print 'YES: 4_minutes'
# #elif integration_question1 == "No":
#     #print "NO: zero_minutes"

#     #integration_question1 = input()
#     #total_practice = int(integration_question1)
#     total_practice.append("Integration")


# #total_practice.items()
# #total_practice.keys()
# #total_practice.values()

# print total_practice


# for key in total_practice: 
#     print key 




# integration_question2 = raw_input ("Do you want to add the Intention Series?")
# #print integration_question2
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"
 
# integration_question3 = raw_input ("Do you want to add the Sun Salutation A Series?")
# #print integration_question3
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            
 
# integration_question4 = raw_input ("Do you want to add the Sun Salutation B Series?")
# #print integration_question4
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question5 = raw_input ("Do you want to add the Core Strengthening Series?")
# print integration_question5
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question6 = raw_input ("Do you want to add the Crescent Lunge Series?")
# print integration_question6
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question7 = raw_input ("Do you want to add the Balancing Series?")
# print integration_question7
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question8 = raw_input ("Do you want to add the Triangle Series?")
# print integration_question8
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question9 = raw_input ("Do you want to add the Hip Opener Series?")
# print integration_question9
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question10 = raw_input ("Do you want to add the Spine Strengthening Series?")
# print integration_question10
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question11 = raw_input ("Do you want to add the Forward Fold Series?")
# print integration_question11
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                           
# integration_question12 = raw_input ("Do you want to add the Surrender Series?")
# print integration_question12
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

# integration_question13 = raw_input ("Do you want to add Namaste?")
# print integration_question13
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            



# >>> x = int(raw_input("Please enter an integer: "))
# Please enter an integer: 42000000000000000000000000000000000000000000000000
# >>> if x < 0:0000000000000000
# ...     x = 0
# ...     print 'Negative changed to zero'
# ... elif x == 0:
# ...     print 'Zero'
# ... elif x == 1:
# ...     print 'Single'0000000000000000000000000000000000000000000000
# ... else:
# ...     print 'More'

# print integration_question1
# integration_question2 = raw_input ("Do you want to add the Intention Series?")
# print integration_question2
 
# integration_question3 = raw_input ("Do you want to add the Sun Salutation A Series?")
# print integration_question3                                                                                            
 
# integration_question4 = raw_input ("Do you want to add the Sun Salutation B Series?")
# print integration_question4
 
# integration_question5 = raw_input ("Do you want to add the Core Strengthening Series?")
# print integration_question5
 
# integration_question6 = raw_input ("Do you want to add the Crescent Lunge Series?")
# print integration_question6
 
# integration_question7 = raw_input ("Do you want to add the Balancing Series?")
# print integration_question7
 
# integration_question8 = raw_input ("Do you want to add the Triangle Series?")
# print integration_question8
 
# integration_question9 = raw_input ("Do you want to add the Hip Opener Series?")
# print integration_question9
 
# integration_question10 = raw_input ("Do you want to add the Spine Strengthening Series?")
# print integration_question10
 
# integration_question11 = raw_input ("Do you want to add the Forward Fold Series?")
# print integration_question11
 
# integration_question12 = raw_input ("Do you want to add the Surrender Series?")
# print integration_question12
 
# print integration_question1

# formula to limit the time to between 60-90_min





print total_practice







# integration_question2 = raw_input ("Do you want to add the Intention Series?")
# #print integration_question2
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"
 
# integration_question3 = raw_input ("Do you want to add the Sun Salutation A Series?")
# #print integration_question3
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            
 
# integration_question4 = raw_input ("Do you want to add the Sun Salutation B Series?")
# #print integration_question4
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question5 = raw_input ("Do you want to add the Core Strengthening Series?")
# print integration_question5
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question6 = raw_input ("Do you want to add the Crescent Lunge Series?")
# print integration_question6
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question7 = raw_input ("Do you want to add the Balancing Series?")
# print integration_question7
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question8 = raw_input ("Do you want to add the Triangle Series?")
# print integration_question8
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question9 = raw_input ("Do you want to add the Hip Opener Series?")
# print integration_question9
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question10 = raw_input ("Do you want to add the Spine Strengthening Series?")
# print integration_question10
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

 
# integration_question11 = raw_input ("Do you want to add the Forward Fold Series?")
# print integration_question11
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                           
# integration_question12 = raw_input ("Do you want to add the Surrender Series?")
# print integration_question12
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            

# integration_question13 = raw_input ("Do you want to add Namaste?")
# print integration_question13
# if integration_question1 == "Yes":
#     print 'YES: 4_minutes'
# elif integration_question1 == "No":
#     print "NO: zero_minutes"                                                                                            



# >>> x = int(raw_input("Please enter an integer: "))
# Please enter an integer: 42000000000000000000000000000000000000000000000000
# >>> if x < 0:0000000000000000
# ...     x = 0
# ...     print 'Negative changed to zero'
# ... elif x == 0:
# ...     print 'Zero'
# ... elif x == 1:
# ...     print 'Single'0000000000000000000000000000000000000000000000
# ... else:
# ...     print 'More'

# print integration_question1
# integration_question2 = raw_input ("Do you want to add the Intention Series?")
# print integration_question2
 
# integration_question3 = raw_input ("Do you want to add the Sun Salutation A Series?")
# print integration_question3                                                                                            
 
# integration_question4 = raw_input ("Do you want to add the Sun Salutation B Series?")
# print integration_question4
 
# integration_question5 = raw_input ("Do you want to add the Core Strengthening Series?")
# print integration_question5
 
# integration_question6 = raw_input ("Do you want to add the Crescent Lunge Series?")
# print integration_question6
 
# integration_question7 = raw_input ("Do you want to add the Balancing Series?")
# print integration_question7
 
# integration_question8 = raw_input ("Do you want to add the Triangle Series?")
# print integration_question8
 
# integration_question9 = raw_input ("Do you want to add the Hip Opener Series?")
# print integration_question9
 
# integration_question10 = raw_input ("Do you want to add the Spine Strengthening Series?")
# print integration_question10
 
# integration_question11 = raw_input ("Do you want to add the Forward Fold Series?")
# print integration_question11
 
# integration_question12 = raw_input ("Do you want to add the Surrender Series?")
# print integration_question12
 
# print integration_question1

# formula to limit the time to between 60-90_min




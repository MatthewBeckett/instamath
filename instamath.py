from random import randint

questionfile = open("questions","w")
answerfile = open("answers","w")

columns = 3
rows = 5
skill_level = 2
ref = randint(100000,999999)
title_string = "\n\n\t\t\t\t\tInst-a-test\t\t\tlevel:"+str(skill_level)+"\t   ref:"+str(ref)+"\n\t\t\t\t\t-----------\n\n"
title = False



question = 0

# function - minimum and maximum numbers for random generator controlling difficulty of questions
def minmax(level):
	if level == 1:
		min = 2
		max = 10
	if level == 2:
		min = 2
		max = 50
	if level == 3:
		min = 10
		max = 99
	if level == 4:
		min = 50
		max = 299
	if level == 5:
		min = 100
		max = 999
	if level == 6:
		min = 1000
		max = 9999
	if level == 7:
		min = 1000
		max = 19999
	if level == 8:
		min = 10000
		max = 99999
	values = (min,max,)

	return values


# function - return list of numbers for pattern question 
def getnmbs(level):
	if level == 1:
		value = []*1
		value.append(randint(2,10))

	if level == 2:
		value = []*1
		value.append(randint(-10,-2))

	if level == 3:
		value = []*1
		value.append(randint(-20,20))

	if level == 4:
		value = []*2
		value.append(randint(2,10))
		value.append(randint(-10,-2))

	if level == 5:
		value = []*2
		value.append(randint(-20,20))
		value.append(randint(-20,20))

	if level == 6:
		value = []*3
		value.append(randint(-20,20))
		value.append(randint(-20,20))
		value.append(randint(-20,20))

	if level == 7:
		value = []*3
		value.append(randint(-50,50))
		value.append(randint(-50,50))
		value.append(randint(-50,50))

	if level == 8:
		value = []*3
		value.append(randint(-100,100))
		value.append(randint(-100,100))
		value.append(randint(-100,100))
	
	return value

# function - rowadnmb
def rndcln():
        val = randint(0,5)
        if val == 0:
                return (val, 4)
        elif val == 1:
                return (val, 4)
        elif val == 2:
                return (val, 1)
        elif val == 3:
                return (val, 4)
	elif val == 4:
                return (val, 4)
	elif val == 5:
                return (val, 1)



# funtion - number spacing and number to string 
def spaceno(number):
	if number < 10:
           	number = "    "+str(number)
        elif number < 100:
                number = "   "+str(number)
        elif number < 1000:
                number = "  "+str(number)
        elif number < 10000:
                number = " "+str(number)
        elif number < 100000:
                number = str(number)

	return number

# function - random question chooser
def qstlst():
	return (addQ(skill_level), subQ(skill_level), patQ(skill_level), mltQ(skill_level), divQ(skill_level), spdQ(skill_level))


# function - adding question
def addQ(level):	
	q =[[] for z in range(2)]

	mimale = minmax(level)	

        for y in range(0,2):
        	q[y] = randint(mimale[0],mimale[1])
                q[y] = spaceno(q[y])

	if int(q[0]) < int(q[1]):
		a = q[0]
		b = q[1]
	else:
		a = q[1]
		b = q[0]

	sum = []*14	
        sum.append("")		
        sum.append("")	
	sum.append("        ")
        sum.append("\t\t"+a)
        sum.append("\t+\t"+b)
        sum.append("\t_____________")
        sum.append("\t             ")
        sum.append("\t_____________")
        while len(sum) < 12:
        	sum.append("")
	# answer
	sum.append(str(int(a)+int(b)))

	return sum

# function - random equation question
def equQ(level):
	nmbs1 = []*level
	nmbs2 = []*level

	line = []*level
	answer = []*level
	
	for x in level:
		nmbs.append(randint(2,randint(3,20*level)))
		y = randint(0,3)
		if y == 0:
			answer[x] = nmbs1 + nmbs2
			line[x] = ("("+str(nmbs1)+"+"+str(nmbs2)+")" )		
		elif y == 1:
			answer[x] = nmbs1 - nmbs2
			line[x] = ("("+str(nmbs1)+"-"+str(nmbs2)+")" )
		elif y == 2:
			answer[x] = nmbs1 * nmbs2
			line[x] = ("("+str(nmbs1)+"*"+str(nmbs2)+")" )
		elif y == 3:
			answer[x] = float(float(nmbs1) / float(nmbs2))
			line[x] = ("("+str(nmbs1)+"/"+str(nmbs2)+")" )

	

# function - adding question
def spdQ(level):	
	miles = randint(10,(50*level))
	mph = randint(11,350)	

	minutes = int((float(miles) / float(mph))*60)
	hours = minutes / 60
	minutes = minutes % 60        

	y = randint(0,2)
	z = randint(0,1)	

	mph = str(mph)
	miles = str(miles)
	hours = str(hours)
	minutes = str(minutes) 

	answer = ""

	line = []*4
	if y == 0:
		line.append( "If a train had traveled "+miles+" miles ")
		if z == 0:
			line.append("at a constant speed of "+mph+"mph,")
			line.append("how long would it of taken?")
			line.append("hours = ______   minutes = ______")
			answer = hours+" hours\t"+minutes+" minutes"
			
		else:
			line.append("in a time of "+hours+" hours and "+minutes+" minutes, ")
			line.append("what constant speed would it have traveled?")
			line.append("mph = ______")
			answer = str(mph)+" mph"

	elif y == 1:
		line.append("If a train was traveling at constant "+mph+"mph ")
		if z == 0:
			line.append("for "+miles+" miles, how long would it take?")
			line.append(" ")
			line.append("hours = ______   minutes = ______")
			answer = hours+" hours\t"+minutes+" minutes"
					
		else:
			line.append("for "+hours+" hours and "+minutes+" minutes,")
			line.append("how far would it have traveled? ")
			line.append("miles = ______")
			answer = miles+" miles"
	else:
		line.append("If a train had traveled for "+hours+" hours and "+minutes+" minutes ")
		if z == 0:
			line.append("at a constant speed of "+mph+"mph,")
			line.append("how far would it have traveled?")
			line.append("miles = ______")
			answer = miles+" miles"
		else:
			line.append("for "+miles+" miles,") 
			line.append("what would the constant speed be?")
			line.append("mph = ______")
			answer = mph+" mph"
	
	sum = []*14	
        sum.append("\t\t\t")		
        sum.append("\t\t\t")	
	sum.append("\t\t\t")
        sum.append("\t\t\t")
        sum.append("\t"+line[0]+line[1])
        sum.append("\t"+line[2])
        sum.append("\t             ")
        sum.append("\t"+line[3])
        while len(sum) < 12:
        	sum.append("")
	# answer
	sum.append(answer)

	return sum

# function - division question
def divQ(level):	
	q =[[] for z in range(2)]

	mima = minmax(level)	

	a = randint(2,5*skill_level)        
	b = randint(mima[0],mima[1])        

	while b < a:
		b = randint(10,50)

	line = []*2
	line.append("\t"+str(a)+"|"+str(b))
	line.append(" ")
	
	while len(line[0]) < 13:
		line[0] = line[0]+" "
	for x in range(0,len(str(a))):
		line[1] = line[1]+" " 

	line[1] += "______"

	sum = []*14	
        sum.append("")
        sum.append("")	
        sum.append("\t")	
	sum.append("\t"+line[1])
        sum.append(line[0])
        for y in range(0,len(str(int(b)))):
		sum.append("\t\t")
        sum.append("\t_____________")
	while len(sum) < 12:
        	sum.append("\t\t")
	# answer
	sum.append(str(int(b)/int(a))+"\tr"+str(int(b)%int(a)))

	return sum



# function - subtracting question
def subQ(level):			
	q =[[] for z in range(2)]

	mimale = minmax(level)	

	# space number
        for y in range(0,2):
        	q[y] = randint(mimale[0],mimale[1])
		q[y] = spaceno(q[y])
                
	# higher number at the bottom
	if int(q[0]) < int(q[1]):
		a = q[0]
		b = q[1]
	else:
		a = q[1]
		b = q[0]

	sum = []*14	
        sum.append("")		
        sum.append("")	
	sum.append("        ")
        sum.append("\t\t"+a)
        sum.append("\t-\t"+b)
        sum.append("\t_____________")
        sum.append("\t             ")
        sum.append("\t_____________")
        while len(sum) < 12:
        	sum.append("")
	# answer
        sum.append(str(int(b)-int(a)))

	return sum

# function - subtracting question
def mltQ(level):			
	q =[[] for z in range(2)]

	mimale = minmax(level)	

	# space number
        for x in range(0,2):
        	q[x] = randint(mimale[0],mimale[1])
		q[x] = spaceno(q[x])
                
	# higher number at the bottom
	if int(q[0]) < int(q[1]):
		a = q[0]
		b = q[1]
	else:
		a = q[1]
		b = q[0]

	sum = []*14			
        sum.append("")
        sum.append("\t\t")	
	sum.append("        ")
        sum.append("\t\t"+a)
        sum.append("\tx\t"+b)
        sum.append("\t_____________")
	for y in range(0,len(str(int(b)))):
		sum.append("\t\t")
        sum.append("\t_____________")
	while len(sum) < 12:
        	sum.append("\t\t")
	# answer
        sum.append(str(int(b)*int(a)))

	return sum



# function - pattern question
def patQ(level):

	nmbs = getnmbs(level)
	if level > 1:
		mima = minmax(int(level) / 2)
	else:
		mima = minmax(level)
	
	srcnmb = randint(mima[0],mima[1])
	val = []*10
	val.append(str(srcnmb))	

	nmbidx = 0
	for x in range(1,10):

		nmbidx +=1
		if nmbidx > len(nmbs)-1:
			nmbidx = 0

		srcnmb = srcnmb + nmbs[nmbidx]
		val.append(str(srcnmb))

	
	ansidx = randint(0,8)
	
	answer = val[ansidx]


	a =""
	b =""

	for y in range(0,9):
		if ansidx == y:
			a +="A"+"\t"
		else:
			a +=str(val[y])+"\t" 

	sum = []*14	
        sum.append("")		
        sum.append("")	
	sum.append("\t\t\t\t\t\t\t\t\t")
        sum.append("\t")
        sum.append("\t"+a)
        sum.append("\t")	
        sum.append("\t")
        sum.append("\tA = _________"+"\t\t\t\t\t\t\t\t")
        while len(sum) < 12:
        	sum.append("")
	# answer
        sum.append(str(answer))

	return sum
	
# Main -------------------------------------------------------------------

for o in range(0,rows):
	
	sums =[[] for i in range(100)]

	answers = []*(100)

	qsttyp = rndcln()
	columns = qsttyp[1]
	

	for x in range(0,columns):
		
		question +=1		
	
		sum = qstlst()[qsttyp[0]]        	

		sums[x].append(sum[0]+"\t")
		sums[x].append(sum[1]+"\t")        	
		sums[x].append("\t"+str(question)+"."+sum[2]+"\t")        			
        	sums[x].append(sum[3]+"\t")
        	sums[x].append(sum[4]+"\t")
        	sums[x].append(sum[5]+"\t")
        	sums[x].append(sum[6]+"\t")
        	sums[x].append(sum[7]+"\t")
		sums[x].append(sum[8]+"\t")
		sums[x].append(sum[9]+"\t")
		sums[x].append(sum[10]+"\t")
		sums[x].append(sum[11]+"\t")
		sums[x].append(sum[12]+"\t")

		answerfile.write(str(question)+".\t- "+sums[x][12]+"\n")
		
	for x in range(0,12):
		line = ""
		for i in range(0,columns):
			line += sums[i][x]
		if title == False:
			title = True
			questionfile.write(title_string)

		questionfile.write(line+"\n")

# -------------------------------------------------------------------------

	

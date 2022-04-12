
def arithmetic_arranger(operations,results=False):
    line1=""
    line2=""
    line3=""
    line4=""
    formatter = ""

    if len(operations) > 5:
        formatter = "Error: Too many problems."
        return formatter 

    for operation in operations:
        operator1 = operation.split(" ")[0]
        op = operation.split(" ")[1]
        operator2 = operation.split(" ")[2]

        if op!="+" and op!="-":
            formatter = "Error: Operator must be '+' or '-'."
            return formatter
        if len(operator1)>4 or len(operator2)>4:
            formatter = "Error: Numbers cannot be more than four digits."
            return formatter    
        
        if operator1.isdigit()==False or operator2.isdigit()==False:
            formatter = "Error: Numbers must only contain digits."
            return formatter 

        if len(line1)>0:
            line1+="    "        
            line2+="    "        
            line3+="    "        
            line4+="    " 
          
        line1+="  "
        line2+=op+" "
       
        
        for i in range(max(len(operator1),len(operator2))-min(len(operator1),len(operator2))):
            if len(operator1) > len(operator2):
                line2+=" "
            else:
                line1+=" "  
         
        for i in range(max(len(operator1),len(operator2))+2):
            line3+="-"

        if(op=="+"):
            result = int(operator1)+int(operator2)
        else:
            result = int(operator1)-int(operator2)    

        for i in range(max(len(operator1),len(operator2))+2-len(str(result))):
            line4+=" "

        line1+=operator1
        line2+=operator2
        line4+=str(result)
             

    result = line1 + "\n" + line2 + "\n" + line3
    if(results):
        result+= "\n" + line4 
    return result  
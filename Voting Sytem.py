# Task to register candidate name who want to participate in election
candidate = []
for i in range(1, 5):
    
    
    candidate_name = input(&quot;Enter your candidate name :&quot;)
    candidate.append(candidate_name)
    n = len(candidate)
    if  n<4:
    
    
        print(&quot;You have been successfully registered&quot;)
    else :
        print(&quot;Maximum candidate have been enrolled&quot;)


# Task to register candidate who want to caste their vote  
voter = []
number = int(input(&quot;Enter total number of voter want to cast their vote :&quot;))
for i in range(1,number + 1):
    voter_id = int(input(&quot;Enter voter id number :&quot;))
    voter.append(voter_id)


while True :
    if voter ==[]:
        print(&quot;Voting session is over&quot;)
        max = candidate_1_votes
        if candidate_2_votes &gt; max:
            max = candidate_2_votes
            percent = (candidate_2_votes/num_of_voter)*100
            print(candidate[1],&quot;has won&quot;,&quot;with&quot;,percent,&quot;% votes&quot;)
            break
        elif candidate_3_votes &gt; max:
            max = leader_3_votes
            percent = (leader_3_votes/num_of_voter)*100
            print(candidate[2],&quot;has won&quot;,&quot;with&quot;,percent,&quot;% votes&quot;)
            break
        elif candidate_4_votes &gt; max:
            max = leader_4_votes
            percent = (candidate_4_votes/num_of_voter)*100
            print(candidate[3],&quot;has won&quot;,&quot;with&quot;,percent,&quot;% votes&quot;)
            break
        else :
            percent = (leader_1_votes/num_of_voter)*100
            print(candidate[0],&quot;has won&quot;,&quot;with&quot;,percent,&quot;% votes&quot;)
            break
         
         
    else :   
         voter_id = int(input(&quot;Enter your voter-id no :&quot;))
         if voter_id in voter:
            print(&quot;You are a voter &quot;)
            voter.remove(voter_id)
            print(&quot;========================================================\n&quot;)
            print(&quot;Here are the list of candidate name :&quot;)
            print(&quot; 1. candidate -1 : &quot;, candidate[0],
                  &quot;\n 2. candidate -2 :&quot;, candidate[1],
                  &quot;\n 3. candidate -3 :&quot;, candidate[2],
                  &quot;\n 4. candidate -4 :&quot;, candidate[3])
             
            vote = int(input(&quot;Cast your vote for candidate1 or candidate2 or candidate3 or candidate4 or leader5  :\n&quot;
             &quot; Write only sr. no of candidate (like 1 or 2):\n&quot;))
            print(&quot;===========================================================\n&quot;)
            if vote == 1:
               candidate_1_votes+=1
               print(&quot;Thank you for casting your vote &quot;)
            elif vote == 2:
               candidate_2_votes+=1
               print(&quot;Thank you for casting your vote&quot;)
            elif vote == 3:
               candidate_3_votes+=1
               print(&quot;Thank you for casting your vote&quot;)
            elif vote == 4:
               candidate_4_votes+=1
               print(&quot;Thank you for casting your vote&quot;)
            
            else :
                print(&quot;Leader is not found \n Please enter correct candidate number&quot;)
         
         
         else :
                
               print("You have already voted or invalid voter id ")

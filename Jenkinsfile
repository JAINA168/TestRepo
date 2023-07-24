

pipeline {
    agent any
    environment{
 	autosys_main_server= 'amraelp00011108'
	jilDirectory='autosys/'
	apiEndpoint='https://amraelp00011055.pfizer.com:9443/AEWS/jil'
    }
    parameters {
        //choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Autosys Environment', name: 'Deploy_to_Autosys'
	    choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Unix Environment', name: 'Deploy_to_Unix'
       
    }
    stages{
        
        
	 stage ("Deploy to Unix"){
            when {
                 expression { params.Deploy_to_Unix == "Yes" }
            }
                steps{
                    script{
        	      sh "scp -i /var/lib/jenkins/.ssh/id_rsa -r test1.py srvamr-sfaops@amer@amraelp00011593:/tmp"
		      sh "ssh -i /var/lib/jenkins/.ssh/id_rsa srvamr-sfaops@amer@amraelp00011593 'sudo chmod 775 /tmp*'"
		
		    }
                }
        }
            
				
        }
    }




pipeline {
    agent any
    environment{
 	autosys_main_server= 'amraelp00011593'
	jilDirectory='autosys/'
	autosys_apiEndpoint='https://amraelp00011107.pfizer.com:9443/AEWS/jil'
    }
    parameters {
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Autosys Environment', name: 'Deploy_to_Autosys'
	choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Unix Environment', name: 'Deploy_to_Unix'
       
    }
    stages{
        
        
	 stage ("Deploy to Unix"){
            when {
                 expression { params.Deploy_to_Unix == "Yes" }
            }
                steps{
                    script{
        		//sh "scp -i /var/lib/jenkins/.ssh/id_rsa -r test1.py srvamr-sfaops@amer@amraelp00011593:/tmp"
			//sh "ssh -i /var/lib/jenkins/.ssh/id_rsa srvamr-sfaops@amer@amraelp00011593 'sudo chmod 755 /tmp/test1.py'"
				//testing /app/etl/palign/scripts/
			   // scp -i /var/lib/jenkins/.ssh/id_rsa -r ./python_scripts/batch_configurations.ini ./python_scripts/batch_process.py srvamr-sfaops@amer@amraelp00011593:/app/etl/palign/scripts/scripts_ui/python_scripts
			sh "scp -i /var/lib/jenkins/.ssh/id_rsa -r test1.py srvamr-sfaops@amer@amraelp00011593:/app/etl/palign/scripts/scripts_ui/python_scripts"
			sh "ssh -i /var/lib/jenkins/.ssh/id_rsa srvamr-sfaops@amer@amraelp00011593 'sudo chmod 755 /app/etl/palign/scripts/scripts_ui/python_scripts/*'"
			    //testing /app/etl/palign/parameter_files/
			//sh "scp -i /var/lib/jenkins/.ssh/palign_id_rsa -r test1.py srvamr-palign@amer@amraelp00011593:/app/etl/palign/parameter_files/"
			//sh "ssh -i /var/lib/jenkins/.ssh/palign_id_rsa srvamr-palign@amer@amraelp00011593 'sudo chmod 755 /app/etl/palign/parameter_files/*'"
			    //testing /app/etl/palign/scripts/scripts_ui/python_scripts
			//sh "scp -i /var/lib/jenkins/.ssh/palign_id_rsa -r test1.py srvamr-palign@amer@amraelp00011593:/app/etl/palign/scripts/scripts_ui/python_scripts/"
			//sh "ssh -i /var/lib/jenkins/.ssh/palign_id_rsa srvamr-palign@amer@amraelp00011593 'sudo chmod 755 /app/etl/palign/scripts/scripts_ui/python_scripts/*'"
			    //testing /home/srvamr-palign/.snowsql
			//sh "scp -i /var/lib/jenkins/.ssh/palign_id_rsa -r test1.py srvamr-palign@amer@amraelp00011593:/home/srvamr-palign/.snowsql/"
			//sh "ssh -i /var/lib/jenkins/.ssh/palign_id_rsa srvamr-palign@amer@amraelp00011593 'sudo chmod 755 /home/srvamr-palign/.snowsql/*'"
		    }
                }
        }
        stage ("Deploy to Autosys"){
            when {
                 expression { params.Deploy_to_Autosys == "Yes" }
            }
            steps{		
		        sh 'curl -X POST -H "Content-Type: text/plain" --upload-file "${jilFile}" ${autosys_apiEndpoint} -k --user "srvamr-sfaops:0wO:v%He[a;_HzdFYkyKwS34g" -i	'		
		        }
            }
				
        }   
				
        
    }




pipeline {
    agent any
    environment{
 	autosys_main_server= 'amraelp00011593'
	jilDirectory='autosys/'
	autosys_apiEndpoint='https://amraelp00011055.pfizer.com:9443/AEWS/jil'
	unix_server = "amrvopsfa000001"
        unix_src_path_scripts = "autosys/"
        unix_deploy_path_scripts = "/tmp"
        unix_service_account = "srvamr-palign@amer"
        unix_permission = "775"
    }
    parameters {
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Autosys Environment', name: 'Deploy_to_Autosys'
	choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Unix Environment', name: 'Deploy_to_Unix'
	choice choices: ['Yes', 'No'], description: 'Mention if You want to Dry Run', name: 'dry_run'    
       
    }
    stages{
        stage ("Deploy to Unix"){
            when {
                 expression { params.Deploy_to_Unix == "Yes" }
            }
                steps{
                    script{
                        // Call unix.groovy passing parameters
                    	def unixParams = [
                        	src: unix_src_path_scripts,
                        	dest: unix_deploy_path_scripts,
                        	server: unix_server,
                        	service_account: unix_service_account,
                        	permissions: unix_permission,
                        	dry_run: params.dry_run // Pass the dry_run parameter
                    	]

                    	load "unix.groovy"
			deployToUnix(unixParams)
                        }
                }
        }
        
        stage ("Deploy to Autosys"){
            when {
                 expression { params.Deploy_to_Autosys == "Yes" }
            }
           
		steps{		
		        sh 'chmod +x devops_scripts/autosys_deploy.sh' 
		        withCredentials([usernamePassword(credentialsId: 'sfaops', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
        		    script {
            			env.PASSWORD = sh(script: "echo \$PASSWORD", returnStdout: true).trim()
            			env.USERNAME = sh(script: "echo \$USERNAME", returnStdout: true).trim()
        		    } 	
			    sh "devops_scripts/autosys_deploy.sh ${params.dry_run}" // Pass the params			
		        }
            }	
        }
				
        }   
				
        
    }

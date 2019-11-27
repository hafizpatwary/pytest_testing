pipeline{
	agent any

	stages{
		stage('--Install pytest as Jenkins--'){
			steps{
				sh "sudo apt install python3-pip"
				sh "pip3 install pytest"
				sh "sudo apt install python-pytest"
			}
		}
		stage('--Printing current working directorty--'){
			steps{
				sh "pwd "
			}
		}
		stage('--Test--'){
			steps{
				sh "pytest"
			}
		}
		stage('--list--'){
			steps{
				sh "echo 'previous stage worked'"
			}
		}
	}
}
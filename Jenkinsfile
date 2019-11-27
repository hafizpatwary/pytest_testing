pipeline{
	agent any

	stages{
		stage('--Install pytest as Jenkins--'){
			steps{
				sh "pip3 install pytest"
				sh "pip3 --version"
				sh "whereis pip3"
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
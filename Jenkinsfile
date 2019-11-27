pipeline{
	agent any

	stages{
		stage('--Install pytest as Jenkins--'){
			steps{
				sh "pip3 install pytest"
				sh "pytest"
			}
		}
		stage('--Printing current working directorty--'){
			steps{
				sh "pwd "
			}
		}
		stage('--list--'){
			steps{
				sh "echo 'previous stage worked'"
			}
		}
	}
}
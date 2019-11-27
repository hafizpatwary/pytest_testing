pipeline{
	agent any

	stages{
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
				sh "echo previous stage worked"
			}
		}
	}
}
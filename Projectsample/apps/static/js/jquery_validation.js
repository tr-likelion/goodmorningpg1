$("#signup_form").validate({

	rules: { //규칙 부분

		name: {

				required: true, // 두 가지 규칙 이상 추가 시.
				minlength: 2 // 최소 길이 2 이상

			},

			password: {

				required: true,
				minlength: 5

			},

			confirm_password: {

				required: true,
				minlength: 5,

			equalTo: "#signup-password" // id가 password인 input과 값이 같아야 함

		},

		email: {

			required: true,
			email: true // e-mail 유형인지 검사함

		},

	},

	messages: { // 유효성 검사에서 부적합함이 적발된 경우

		name: {

			required: "Please enter a username", // 규칙이 여러개일 땐, 각 규칙에 대응해서 메시지를 띄워줍니다.
			minlength: "Your username must consist of at least 2 characters"

		},

		password: {

			required: "Please provide a password",
			minlength: "Your password must be at least 5 characters long"

		},

		confirm_password: {

			required: "Please provide a password",
			minlength: "Your password must be at least 5 characters long",
			equalTo: "Please enter the same password as above"

		},

		email: "Please enter a valid email address"

	}

});

$("#login_form").validate({

	rules: { //규칙 부분

		password: {

			required: true,
			minlength: 5

		},

		email: {

			required: true,
			email: true // e-mail 유형인지 검사함

		},

	},

	messages: { // 유효성 검사에서 부적합함이 적발된 경우

		password: {

			required: "Please provide a password",
			minlength: "Your password must be at least 5 characters long"

		},

		email: "Please enter a valid email address"

	}

});

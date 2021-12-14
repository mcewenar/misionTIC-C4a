<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label>lastname</label>
                        <div class="control">
                            <input type="text" class="input" v-model="lastname">
                        </div>
                    </div>

                    <div class="field">
                        <label>email</label>
                        <div class="control">
                            <input type="text" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Sign up</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/log-in">click here</router-link> to log in!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import gql from "graphql-tag";



export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            name:'',
            lastname:'',
            email: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        submitForm: async function() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing')
            }

            if (this.password === '') {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    name: this.name,
                    lastname: this.lastname,
                    email: this.email,
                    password: this.password,

                }
                await this.$apollo
                    .mutate({
                    mutation: gql`
                        mutation($userInput: SignUpInput!) {
                            signUpUser(userInput: $userInput) {
                                refresh
                                access
                            }
                        }
                    `,
                    variables: {
                        userInput: formData,
                    },
                    })
                    .then((result) => {
                        let dataLogIn = {
                            username: formData.username,
                            token_access: result.data.signUpUser.access,
                            token_refresh: result.data.signUpUser.refresh,
                        };
                    this.$emit("completedSignUp", dataLogIn);
                    //this.$App.completedSignUp
                    console.log("entro en emit");
                    })
                    .catch((error) => {
                    alert("ERROR: Fallo en el registro.");
                    });

            }
        }
    }
}
</script>
<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Log In</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/sign-up">Click Aqui</router-link> para Registrarte!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import gql from 'graphql-tag';
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In | Nous'
    },
    methods: {
        submitForm: async function(){
            const formData = {
                    username: this.username,
                    password: this.password,

                }
            await this.$apollo
            .mutate({
                mutation: gql`
                mutation($credentials: CredentialsInput!){
                    logIn(credentials: $credentials){
                        refresh
                        access
                    }
                }
                `,
                
                variables:{
                    credentials: formData,
                }
                
            })
                .then((result) => {
                    let dataLogIn = {
                        username: formData.username,
                        token_access: result.data.logIn.access,
                        token_refresh: result.data.logIn.refresh,
                    }
                    
                    this.$emit('completedLogIn', dataLogIn)
                })
                .catch((error) => {
                    console.log("aca el error:")
                    console.log(error)
                    if (error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                    
                });
        }
        }
}
</script>
<template>
    <Header/>
    <div id="signup">
        <h3>注册账号</h3>
        <form>
            <div class="form-elem">
                <span>账号：</span>
                <input v-model="signupName" type="text" placeholder="输入用户名">
            </div>
            <div class="form-elem">
                <span>密码：</span>
                <input v-model="signupPwd" type="password" placeholder="输入密码">
            </div>
            <div class="form-elem">
                <button v-on:click.prevent="signUp">提交</button>
            </div>
        </form>
    </div>

    <div id="signIn">
        <form>
            <div class="form-elem">
                <span>账号：</span>
                <input v-model="signinName" type="text" placeholder="输入用户名">
            </div>

            <div class="form-elem">
                <span>密码：</span>
                <input v-model="signinPwd" type="password" placeholder="输入密码">
            </div>

            <div class="form-elem">
                <button v-on:click.prevent="signIn">登录</button>
            </div>
        </form>
    </div>
    <Footer/>
</template>

<script>
import axios from "axios";
import Header from "@/views/Header";
import Footer from "@/views/Footer";

export default {
    name: "Login",
    components: {Header, Footer},
    data: function () {
        return {
            signupName: '',
            signupPwd: '',
            signupResponse: null,

            signinName: '',
            signinPwd: '',
        }
    },
    methods: {
        signUp() {
            const that = this;
            axios
                .post('/api/user/', {
                    username: that.signupName,
                    password: that.signupPwd
                })
                .then(function (response) {
                    that.signupResponse = response.data;
                    alert('用户注册成功，快去登录吧！');
                })
                .catch(function (error) {
                    alert(error.message)
                })
        },
        signIn() {
            const that = this;
            axios
                .post('/api/token/', {
                    username: that.signinName,
                    password: that.signinPwd,
                })
                .then(function (response) {
                    const storage = localStorage;
                    const expiredTime = Date.parse(response.headers.date) + 60000;

                    storage.setItem("access.graduation", response.data.access);
                    storage.setItem('refresh.graduation', response.data.refresh);
                    storage.setItem('expiredTime.graduation', expiredTime);
                    storage.setItem('username.graduation', that.signinName);

                    that.$router.push({name: 'Home'})
                })
                .catch(function (error) {
                    alert("signin:" + error.message)
                })
        }
    }
}
</script>

<style scoped>
#grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
}

#signup {
    text-align: center;
}
#signIn {
    text-align: center;
}
.form-elem {
    padding: 10px;
}

input {
    height: 25px;
    padding-left: 10px;
}

button {
    height: 35px;
    cursor: pointer;
    border: none;
    outline: none;
    background: gray;
    color: whitesmoke;
    border-radius: 5px;
    width: 60px;
}
</style>
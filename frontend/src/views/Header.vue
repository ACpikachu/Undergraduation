<template>
    <div id="header">
        <div class="grid">
            <div></div>
            <h1>My Drf-Vue graduation project</h1>
            <search-button></search-button>
        </div>

        <hr>

        <div class="login">
            <div v-if="hasLogin">
                欢迎、欢迎 {{ username }} !!!
            </div>
            <div v-else>
                <router-link to="/login" class="login-link">登陆</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import SearchButton from "@/views/searchButton";

export default {
    name: 'Header',
    components: {SearchButton},
    data: function () {
        return {
            username: '',
            hasLogin: false
        }
    },
    methods: {

    },
    mounted() {
        const that = this;
        const storage = localStorage;
        const expiredTime = Number(storage.getItem("expiredTime.graduation"));
        //当前时间
        const current = (new Date()).getTime();
        //刷新令牌
        const refreshToken = storage.getItem("refresh.graduation");
        // 用户名
        that.username = storage.getItem('username.graduation');

        //令牌还没有过期的时候
        if (expiredTime > current) {
            that.hasLogin = true
        } else if (refreshToken !== null) {
            axios
                .post('/api/token/refresh/', {
                    refresh: refreshToken
                })
                .then(function (response) {
                    const nextExpiredTime = Date.parse(response.headers.date) + 60000;

                    storage.setItem('access.graduation', response.data.access);
                    storage.setItem('expiredTime.graduation', nextExpiredTime);
                    storage.removeItem('refresh.graduation');

                    that.hasLogin = true;
                })
                .catch(function () {
                    // .clear() 清空当前域名下所有的值
                    // 慎用
                    storage.clear();
                    that.hasLogin = false;
                })
        } else {
            storage.clear();
            that.hasLogin = false
        }

    }

}
</script>

<style scoped>
#header {
    text-align: center;
    margin-top: 20px;
}

.search {
    padding-top: 22px;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 4fr 1fr;
}
</style>
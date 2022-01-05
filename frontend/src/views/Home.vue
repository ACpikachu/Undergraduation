<!--
 * @Date                : 2021-12-27 19:38:56
 * @LastEditors         : 王少帅
 * @LastEditTime        : 2021-12-27 19:38:56
 * @FilePath            : /drf_vue_blog/frontend/src/App.vue
-->
<template>
    <Header></Header>

    <ArticleList></ArticleList>

    <Footer></Footer>
</template>

<script>
import axios from "axios";
import Header from "@/views/Header";
import ArticleList from "@/views/ArticleList";
import Footer from "@/views/Footer";
export default {
    name: "Home",
    components: {Header, Footer, ArticleList},
    data: function () {
        return {
            info: "",
        };
    },
    mounted() {
        axios.get("/api/article").then((response) => (this.info = response.data));
    },
    methods: {
        formatted_time: function (iso_date_string) {
            const date = new Date(iso_date_string);
            return date.toLocaleDateString()
        }
    }
};
</script>

<style>
#app {
    font-family: Georgia, Arial, sans-serif;
    margin-left: 40px;
    margin-right: 40px;
}
</style>

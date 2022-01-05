<!--
 * @Date                : 2021-12-30 14:52:32
 * @LastEditors         : 王少帅
 * @LastEditTime        : 2021-12-30 14:52:32
 * @FilePath            : /grauation_project/frontend/src/views/ArticleDetail.vue
-->
<template>

    <Header/>

    <div v-if="article !== null" class="grid-container">
        <div>
            <h1 id="title">{{ article.title }}</h1>
            <p id="subtitle">
                本文由 {{ article.author.username }} 发布于 {{ formatted_time(article.created) }}
            </p>
            <div v-html="article.body_html" class="article-body"></div>
        </div>
        <div>
            <h3>目录</h3>
            <div v-html="article.toc_html" class="toc"></div>
        </div>
    </div>

    <Footer/>

</template>

<script>
import Header from "@/views/Header";
import Footer from "@/views/Footer";

import axios from 'axios';


export default {
    name: 'ArticleDetail',
    components: {Header,Footer},
    data: function () {
        return {
            article: null
        }
    },
    mounted() {
        axios
            .get('/api/article/' + this.$route.params.id)
            .then(response => (this.article = response.data))
    },
    methods: {
        formatted_time: function (iso_date_string) {
            const date = new Date(iso_date_string);
            return date.toLocaleDateString()
        }
    }
}
</script>

<style scoped>
.grid-container {
    display: grid;
    grid-template-columns: 3fr 1fr;
}


#title {
    text-align: center;
    font-size: x-large;
}

#subtitle {
    text-align: center;
    color: gray;
    font-size: small;
}

</style>

<style>
.article-body p img {
    max-width: 100%;
    border-radius: 50px;
    box-shadow: gray 0 0 20px;
}

.toc ul {
    list-style-type: none;
}

.toc a {
    color: gray;
}
</style>
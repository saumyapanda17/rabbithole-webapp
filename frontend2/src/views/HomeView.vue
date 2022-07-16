<template>
  <div class="home">
    <div class="container mt-4">
      <h1>Latest Questions</h1>
      <br />
      <div class="card" v-for="question in questions" :key="question.pk">
        <p class="card card-header">
          Posted by:
          <span class="question-author">{{ question.author }}</span>
        </p>
        <h2 class="card-body">
          <router-link
            :to="{ name: 'question', params: { slug: question.slug } }"
            class="question-link"
            >{{ question.content }}
          </router-link>
        </h2>
        <p class="card-footer">Comments: {{ question.answers_count }}</p>
      </div>
      <br />
      <br />
      <br />
      <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
        <button
          v-show="next"
          @click="getQuestions"
          class="btn btn btn-outline-dark"
        >
          Load More
        </button>
      </div>
      <br />
      <br />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "HomeView",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false,
    };
  },
  methods: {
    getQuestions() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint).then((data) => {
        this.questions.push(...data.results);
        this.loadingQuestions = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
  },
  created() {
    this.getQuestions();
    document.title = "RABBITHOLE";
  },
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: rgb(160, 42, 81) !important;
}

h1 {
  font-weight: 700;
}

.question-link {
  font-weight: bold;
  color: black;
}

.question-link:hover {
  color: #343a40;
  text-decoration: none;
}

.mb-0 {
  font-size: 80%;
}
p {
  margin-bottom: 0;
}
.card {
  margin-bottom: 2%;
}
.card-body {
  margin: 0;
}
</style>

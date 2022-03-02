<template>
  <div class="container">
    <div class="row text-center" v-if="error">
      <h1 class="text-danger">{{ error }}</h1>
      <h3>Add "/?reg=YourRegNumber" to the url and try again</h3>
    </div>
    <div class="row text-center" v-if="details">
      <div class="col-sm-10">
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Registration</th>
              <th scope="col">Make</th>
              <th scope="col">Model</th>
              <th scope="col">Colour</th>
              <th scope="col">Engine size</th>
              <th scope="col">Year</th>
              <th scope="col">MOT due date</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ details.registration }}</td>
              <td>{{ details.make }}</td>
              <td>{{ details.model }}</td>
              <td>{{ details.primaryColour }}</td>
              <td>{{ details.engineSize}}cc</td>
              <td>{{ details.firstUsedDate.split(".")[0] }}</td>
              <td>{{ details.motTests[0].expiryDate }}</td>
            </tr>
          </tbody>
        </table>

        <br><br>
        <h3>Mot history ({{ details.motTests.length }} results)</h3>

        <table class="table">
          <thead>
            <tr>
              <th scope="col">Test number</th>
              <th scope="col">Test date</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody v-for="mot in details.motTests" :key="mot.motTestNumber">
            <tr :class="mot.testResult=='PASSED'?' table-success':' table-danger'">
              <td>{{ mot.motTestNumber }}</td>
              <td>{{ mot.completedDate.split(" ")[0].split(".").reverse().join("/") }}</td>
              <td>{{ mot.testResult }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Mot',
  data() {
    return {
      details: '',
      error: '',
    };
  },
  methods: {
    getDetails() {
      const { reg } = this.$route.query;
      const path = `http://localhost:5000/mot?reg=${reg}`;
      axios.get(path)
        .then((res) => {
          if (res.data.error) {
            this.error = res.data.error;
          } else {
            this.details = res.data;
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getDetails();
  },
};
</script>

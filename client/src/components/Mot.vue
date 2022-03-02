<template>
  <div class="container" >
      <p>Reg: {{ details.registration }}</p>
      <p>Make: {{ details.make }}</p>
      <p>Model: {{ details.model }}</p>
      <p>Next MOT due by: {{ details.motTests[0].expiryDate }}</p>
      <p>Past MOTs: {{ details.motTests.length }}</p>
      <ul v-for="mot in details.motTests" :key="mot.motTestNumber">
          <li>{{ mot.motTestNumber }}
              with status {{ mot.testResult }} on {{ mot.completedDate }}
          </li>
      </ul>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Mot',
  data() {
    return {
      details: '',
    };
  },
  methods: {
    getDetails() {
      const { reg } = this.$route.query;
      const path = `http://localhost:5000/mot?reg=${reg}`;
      axios.get(path)
        .then((res) => {
          this.details = res.data;
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

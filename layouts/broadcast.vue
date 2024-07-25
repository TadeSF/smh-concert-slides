<template>
  <div class="flex flex-col h-full">
    <div class="flex justify-center items-center h-52 overflow-hidden p-8">
      <img class="max-h-full max-w-full" src="/Logo_inv.svg" alt="Logo" />
    </div>
    <div
      class="flex-1 flex flex-col justify-center items-center text-center m-10"
    >
      <h1>Rundfunk-Sendetermine</h1>
      <div class="flex flex-col justify-center items-center text-center gap-4">
        <div v-for="(broadcast, index) in broadcasts" :key="index">
          <h2 class="">{{ broadcast.station }} – {{ broadcast.date }}</h2>
          <h3 class="highlight">
            Ab <span class="font-bold"> {{ broadcast.time }}</span> in der
            Sendung "{{ broadcast.title }}"
          </h3>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { onMounted } from "vue";

onMounted(() => {
  if ($slidev.nav.currentPage === $page.value) {
    setTimeout(() => {
      $slidev.nav.nextSlide();
    }, 2000);
  }
});

export default {
  props: {
    broadcasts: { type: Array, default: () => [] },
  },
  computed: {
    test() {
      console.log(this.broadcasts);
      return 1;
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 2em;
  /* Uppercase */
  text-transform: uppercase;
  color: #e5013b;
  margin-bottom: 0.6em;
}

h2 {
  font-size: 1.5em;
  font-weight: bold;
}

h3 {
  font-size: 1.5em;
  font-weight: normal;
  margin-top: 0;
}

.highlight {
  color: #e5013b;
}
</style>

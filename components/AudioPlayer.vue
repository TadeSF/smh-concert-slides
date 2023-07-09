<template>
  <div>
    <audio autoplay style="display: none;">
      <source :src="audioSrc" type="audio/mpeg" />
      Your browser does not support the audio tag.
    </audio>
  </div>
</template>

<script>
export default {
  props: {
    audioSrc: {
      type: String,
      required: true,
    },
  },
};
</script>

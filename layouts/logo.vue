<template>
  <div class="flex flex-col h-full">
    <div class="flex justify-center items-center h-52 overflow-hidden p-8">
      <img src="/Logo_inv.svg" alt="Logo" class="max-h-full max-w-full" />
    </div>
    <div class="flex-1 flex flex-col justify-center items-center text-center" />
  </div>
</template>

<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  overflow: hidden;
  padding: 2em;

}

.logo img {
  max-height: 100%;
  max-width: 100%;
}

.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}


</style>
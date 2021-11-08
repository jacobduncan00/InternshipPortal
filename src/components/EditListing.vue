<template></template>

<script>
export default {
  name: "EditListing",
  async mounted() {
    console.log(this.$route.name);
    let result = await fetch(
      `${process.env.SERVER_URL}/admin/get-listing/${this.listing_type}`
    ).catch((error) => {
      console.log(error);
    });
  },
  data() {
    return {
      listing: {},
    };
  },
};
</script>

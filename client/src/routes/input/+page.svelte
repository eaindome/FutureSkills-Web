<script lang="ts">
    import HeroSection from '$lib/components/ui/HeroSection.svelte';
    import UserInputForm from '$lib/components/ui/UserInputForm.svelte';
    import CallToAction from '$lib/components/ui/CallToAction.svelte';
    
    function handleFormSubmit(event: CustomEvent) {
      const formData = event.detail;
      console.log('Form submitted:', formData);
      // In a real application, you would process this data
      // and then navigate to the dashboard
    }
  </script>
  
<svelte:head>
<title>FutureSkills Coach | Discover Green Careers</title>
<meta name="description" content="Find future-proof careers in green industries and sustainable side hustles to support your transition." />
</svelte:head>

<HeroSection />
<UserInputForm on:formSubmit={handleFormSubmit} />
<CallToAction />
  
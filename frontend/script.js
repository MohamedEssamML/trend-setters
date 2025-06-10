document.addEventListener('DOMContentLoaded', () => {
    async function fetchTrends() {
        try {
            const response = await fetch('http://localhost:5000/api/trends');
            const trends = await response.json();
            const trendsDiv = document.getElementById('trends');
            trendsDiv.innerHTML = trends.map(trend => `
                <div class="trend">
                    <h3>${trend.hashtag}</h3>
                    <p>Views: ${trend.views}</p>
                    <p>Content Idea: ${trend.content}</p>
                </div>
            `).join('');
        } catch (error) {
            console.error('Error fetching trends:', error);
        }
    }
    fetchTrends(); // Call it once on load
});
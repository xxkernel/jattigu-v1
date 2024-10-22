import Header from '../_components/Header';
import AboutPage from '../_pages/AboutPage';
import AboutWithStats from '../_pages/AboutWithStats';
import FooterPage from '../_pages/FooterPage';

export default function Home() {
  return (
    <div className="">
      <Header />
      <AboutWithStats />
      <AboutPage />
      <FooterPage />
    </div>
  );
}

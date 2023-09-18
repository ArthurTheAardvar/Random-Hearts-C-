#include <iostream>
using namespace std;

int MonsterGen(char biome);

int main() {
	int life = 100;
	char biome;
	cout << "What biome will you like to be in (N)ether, (D)esert, (I)ce Spikes or (S)wamp" << endl;
	cin >> biome;
	while (life >= 0) {
		life -= MonsterGen(biome);
		cout << "You currently have " << life << "HP left." << endl;
		cout << "Press any key for next turn." << endl;
		cin >> biome;

	}
	cout << "You Died. Game Over." << endl;
}

int MonsterGen(char biome) {
	int num = rand() % 100;

	if (biome == 'N') {
		if (num < 30) {
			cout << "A Piglin appears!" << endl;
			return 10;
		}
		else if (num < 50) {
			cout << "A Hoglin appears!" << endl;
			return 15;
		}
		else if (num < 80) {
			cout << "A Ghast appears!" << endl;
			return 20;
		}
		else if (num < 90) {
			cout << "A Enderman appears!" << endl;
			return 30;
		}
		else
			cout << "You encountered no one" << endl;
		return 0;
	}
	if (biome == 'D') {
		if (num < 30) {
			cout << "A Husk appears!" << endl;
			return 10;
		}
		else if (num < 50) {
			cout << "A Skeleton appears!" << endl;
			return 15;
		}
		else if (num < 80) {
			cout << "A Phantoms appears!" << endl;
			return 20;
		}
		else if (num < 90) {
			cout << "A Creeper appears!" << endl;
			return 30;
		}
		else
			cout << "You encountered no one" << endl;
		return 0;



	}
	if (biome == 'S') {
		if (num < 30) {
			cout << "A Zombie appears!" << endl;
			return 10;
		}
		else if (num < 50) {
			cout << "A Spider appears!" << endl;
			return 15;
		}
		else if (num < 80) {
			cout << "A Slime appears!" << endl;
			return 20;
		}
		else if (num < 90) {
			cout << "A Creeper appears!" << endl;
			return 30;
		}
		else
			cout << "You encountered no one" << endl;
		return 0;



	}
	if (biome == 'I') {
		if (num < 30) {
			cout << "A Polar Bear appears!" << endl;
			return 40;
		}
		else if (num < 50) {
			cout << "A Frozen Skeleton appears!" << endl;
			return 15;
		}
		else if (num < 80) {
			cout << "A Frozeb Zombie appears!" << endl;
			return 10;
		}
		else if (num < 90) {
			cout << "A Creeper appears!" << endl;
			return 30;
		}
		else
			cout << "You encountered no one" << endl;
		return 0;



	}




}
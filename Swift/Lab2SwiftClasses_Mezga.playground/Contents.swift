//: ## Лабораторная работа №2. Классы Swift
import Foundation
//: Перечесления могут иметь базовый тип. Каждой константе будет присвоено некоторое значение базового типа.
enum Suit: String {
    case spades, hearts, diamonds, clubs
}
Suit.spades.rawValue

enum Rank: Int {
    case two = 2, three, four, five, six, seven,
    eight, nine, ten, jack, queen, king, ace
}
Rank.nine.rawValue
//: Структуры хранятся и передаются по значению (статически). Используйте структуры для хранения набора значений. Если методы объекта позволяют модифицировать хранимые значения, лучше использовать класс.
struct Card {
    let rank: Rank
    let suit: Suit
    
    // Сравнение карт одной масти по старшенству
    static func <(lhv: Card, rhv: Card) -> Bool {
        return lhv.rank.rawValue < rhv.rank.rawValue && lhv.suit == rhv.suit
    }
}
//: ### Задание №1
//: Любой тип можно расширить новыми методами и вычислимыми полями. Принятие протоколов в Swift традиционно реализуется в расширениях.
//:
//: Реализуйте расширение типа `Card` для принятия протокола `CustomStringConvertible`.
//:
//: Свойство `description` должно выводить описание карты на русском: "туз пик".
extension Card: CustomStringConvertible {
    var description: String {
        var descr = ""
        switch self.rank {
        case .two:
            descr.append("двойка")
        case .three:
            descr.append("тройка")
        case .four:
            descr.append("четверка")
        case .five:
            descr.append("пятерка")
        case .six:
            descr.append("шестерка")
        case .seven:
            descr.append("семерка")
        case .eight:
            descr.append("восьмерка")
        case .nine:
            descr.append("девятка")
        case .ten:
            descr.append("десятка")
        case .jack:
            descr.append("валет")
        case .queen:
            descr.append("дама")
        case .king:
            descr.append("король")
        case .ace:
            descr.append("туз")
        }
        switch self.suit {
        case .spades :
            descr.append(" пик")
        case .hearts :
            descr.append(" черв")
        case .clubs :
            descr.append(" треф")
        case .diamonds :
            descr.append(" бубен")
        }
        
        return descr
    }
}

let card = Card(rank: .ace, suit: .spades)
//: Протокол позволяет описать образец некоторого типа, задающий его свойства и методы.
/// Протокол для колоды карт
protocol CardDeck {
    /// Инициализатор для заданных наборов мастей и стоимости
    init(with ranks: [Rank], of suits: [Suit])
    
    /// Снять верхнюю карту
    mutating func getCard() -> Card
    
    /// Колода пуста
    var isEmpty: Bool {get}
}
//: Классы и структуры могут принимать протокол, реализуя запрашиваемые в нём свойства и методы.
class Deck: CardDeck {
    // Внутреннее свойство
    private var cards: [Card]
    
    // Принимаем протокол CardDeck
    
    func getCard() -> Card {
        // мы не перемешивали колоду, поэтому верхняя карта берётся случайно
        return cards.remove(at: Int(arc4random()) % cards.count)
    }
    
    var isEmpty: Bool {
        return cards.isEmpty
    }
    
    // Т. к. протокол принимается классом, инициализатор должен быть помечен required
    // Это гарантирует что любой наследник класса будет иметь этот инициализатор
    required init(with ranks: [Rank], of suits: [Suit] = [.spades, .hearts, .diamonds, .clubs]) {
        self.cards = []
        for suit in suits {
            for rank in ranks {
                self.cards.append(Card(rank: rank, suit: suit))
            }
        }
    }
}
//: Расширения позволяют выносить дополнительную функциональность в отдельный блок кода (или файл).
extension Deck {
    /// Тип колоды: 52, 36, 32 карты
    enum DeckType { case standart52, stripped36, stripped32 }
    
    /// Инициализатор для заданного типа колоды
    convenience init(of type: DeckType) {
        switch type {
        case .standart52:
            self.init(with: [.two, .three, .four, .five, .six, .seven, .eight, .nine, .ten, .jack, .queen, .king, .ace])
        case .stripped36:
            self.init(with: [.six, .seven, .eight, .nine, .ten, .jack, .queen, .king, .ace])
        case .stripped32:
            self.init(with: [.seven, .eight, .nine, .ten, .jack, .queen, .king, .ace])
        }
    }
}

let deck = Deck(of: .standart52)

/// Протокол игрока
protocol CardPlayer {
    /// Имя игрока
    var name: String {get}
    
    /// Инициализатор с заданным именем
    init(withName name: String)
    
    /// Карты в руке
    var hand: [Card] {get}
    
    /// Разыграть карту из руки
    mutating func playCard() -> Card
    
    /// Возвращает карту из руки наименьшей стоимости которая бъёт заданную
    mutating func cover(for card: Card) -> Card?
    
    /// Взять указанную карту в руку
    mutating func take(_ card: Card)
    
    /// Добрать карты в руку из колоды, чтобы стало minNumberOfCards
    mutating func fillHand(from deck: Deck, for minNumberOfCards: Int)
}
//: ### Задание №2
//: Реализуйте класс игрока в карты, принимающий протокол `CardPlayer`.
class Player: CardPlayer {
    let name: String
    
    required init(withName name: String) {
        self.name = name
        self.hand = []
    }
    
    var hand: [Card]
    
    func playCard() -> Card {
        return hand.remove(at: Int(arc4random()) % hand.count)
    }
    
    func cover(for card: Card) -> Card? {
        hand.sort(by: <)
        
        for i in 0..<hand.count {
            if card < hand[i] {
                return hand.remove(at: i)
            }
        }
        return nil
    }
    
    func take(_ card: Card) {
        hand.append(card)
    }
    
    func fillHand(from deck: Deck, for minNumberOfCards: Int) {
        while hand.count < minNumberOfCards && !deck.isEmpty {
            take(deck.getCard())
        }
    }
}
//: Наполните массив игроков:
var players = [CardPlayer]()
var names = ["Александр", "Артём", "Екатерина", "Дина"]

for name in names {
    players.append(Player(withName: name))
}

//: Подобно классам, протоколы можно наследовать, добавляя в них дополнительные требования.
//:
/// Протокол игы
protocol Game {
    /// Уловие завершения игры
    var isFinished: Bool {get}
    /// Начать игру
    mutating func play()
}

/// Протокол карточной игры
protocol CardGame: Game {
    /// Минимальное число карт в руке у игрока
    static var minCardsInHand: Int {get}
    
    /// Колода карт
    var deck: Deck {get}
    
    /// Инициализатор с заданной колодой
    init(with deck: Deck)
    
    /// Игроки
    var players: [CardPlayer] {get}
    
    /// Добавить игрока в игру и выдать ему карты
    mutating func add(player: inout CardPlayer)
}
//: ### Задание №3
//: Реализовать игру в "Дурака" со следующим алгоритмом:
//: ```
//:    Пока количество игроков не равно одному:
//:        Текущий игрок разыгрывает карту
//:        Следующий игрок отбивается
//:
//:        Если следующий игрок не может отбиться, то он берёт разыгранную карту
//:
//:        Если у текущего игрока нет карт, то он выходит из игры
//:        Иначе если его карту не отбили, то добирает до шести карт
//:
//:        Если у следующего игрока нет карт, то он выходит из игры
//:        Иначе добирает до шести карт
//:
//:        Если следующий игрок отбился, то ход переходит к нему
//: ```
//: _Заметьте, что когда игрок выходит из игры, это влияет на индексы игроков в массиве!_
//:
//: В ходе игры необходимо выводить сообщения: "игрок разыграл карту", игрок побил карту, игрок вышел из игры - на консоль, для пояснения хода игры.
class FoolCardGame: CardGame {
    static let minCardsInHand: Int = 6
    
    var deck: Deck
    
    required init(with deck: Deck) {
        self.deck = deck
    }
    
    var players: [CardPlayer] = []
    
    func add(player: inout CardPlayer) {
        players.append(player)
    }
    
    var isFinished: Bool {
        return players.count == 1
    }
    
    //            players[i].fillHand(from: self.deck, for: 6)

    func play() {
        for i in 0..<players.count{
            players[i].fillHand(from: self.deck, for:6)
        }
        var i = 0
        while !isFinished {
            let currentCard = players[i].playCard()
            print("\(players[i].name) разыграл карту \(currentCard)")
            players[i].fillHand(from: self.deck, for: 6)
            
            if players[i].hand.isEmpty {
                print("\(players[i].name) вышел из игры")
                players.remove(at: i)
                i -= 1
            }
            
            let nextI = (i + 1) % players.count
            if let covers = players[nextI].cover(for: currentCard) {
                print("\(players[nextI].name) побил картой \(covers)")
                players[nextI].fillHand(from: self.deck, for: 6)

                i += 1
                i %= players.count
            } else {
                players[nextI].take(currentCard)
                print("\(players[nextI].name) взял карту")
                i += 2
                i %= players.count
            }
            
            if players[nextI].hand.isEmpty {
                print("\(players[nextI].name) вышел из игры")
                players.remove(at: nextI)
                i -= 1
            }
            
            var num_of_cards = ""
            for i in 0..<players.count{
                num_of_cards.append(players[i].name + ": " + String(players[i].hand.count) + " ")
            }
            print(num_of_cards)
        }
    }
}
//: Присвойте `newGame` экземпляр вашей игры. Игра должна начаться автоматически.
var newGame = FoolCardGame(with: Deck(of: .stripped36))

for var player in players {
    newGame.add(player: &player)
}
newGame.play()

if newGame.players.count == 1 {
    print(newGame.players[0].name + " в дураках!")
} else {
    print("Игра завершилась вничью!")
}
//: ### Задание №4 _Дополнительное_
//: Реализовать наследников ваших классов для описания игры с понятием "козырь" (trump suit).
//extension Player {
//    func trumpCover(for card: Card, with trump: Suit) -> Card? {
//        hand.sort(by: <)
//        var trump_found = false
//        var trump_i = 0
//
//        for i in 0..<hand.count {
//            if hand[i].suit == trump && !trump_found {
//                trump_i = i
//                trump_found = true
//            }
//
//            if card < hand[i] {
//                return hand.remove(at: i)
//            }
//        }
//
//        if trump_found {
//            return hand.remove(at: trump_i)
//        }
//        return nil
//    }
//}
//
////
////class TrumpPlayer: Player {
//    func trumpCover(for card: Card, with trump: Suit) -> Card? {
//        hand.sort(by: <)
//        var trump_found = false
//        var trump_i = 0
//
//        for i in 0..<hand.count {
//            if hand[i].suit == trump && !trump_found {
//                trump_i = i
//                trump_found = true
//            }
//
//            if card < hand[i] {
//                return hand.remove(at: i)
//            }
//        }
//
//        if trump_found {
//            return hand.remove(at: trump_i)
//        }
//        return nil
//    }
////}
//
//
//
//
////
//class FoolTrumpGame: FoolCardGame {
//    var trump: Suit
//    required init(with deck: Deck) {
//        let suits: [Suit] = [.clubs, .diamonds, .hearts, .spades]
//        trump = suits.randomElement()!
//
//        super.init(with: deck)
//    }
//
//    override func play() {
//        for i in 0..<players.count{
//            players[i].fillHand(from: self.deck, for:6)
//        }
//        var i = 0
//        print("Козырь в текущей игре: \(trump.rawValue)")
//        while !isFinished {
//            let currentCard = players[i].playCard()
//            print("\(players[i].name) разыграл карту \(currentCard)")
//            players[i].fillHand(from: self.deck, for: 6)
//
//            if players[i].hand.isEmpty {
//                print("\(players[i].name) вышел из игры")
//                players.remove(at: i)
//                i -= 1
//            }
//
//            let nextI = (i + 1) % players.count
//            if let covers = players[nextI].coverTrump(for: currentCard) {
//                print("\(players[nextI].name) побил картой \(covers)")
//                players[nextI].fillHand(from: self.deck, for: 6)
//
//                i += 1
//                i %= players.count
//            } else {
//                players[nextI].take(currentCard)
//                print("\(players[nextI].name) взял карту")
//                i += 2
//                i %= players.count
//            }
//
//            if players[nextI].hand.isEmpty {
//                print("\(players[nextI].name) вышел из игры")
//                players.remove(at: nextI)
//                i -= 1
//            }
//
//            var num_of_cards = ""
//            for i in 0..<players.count{
//                num_of_cards.append(players[i].name + ": " + String(players[i].hand.count) + " ")
//            }
//            print(num_of_cards)
//        }
//    }
//}
////
////var TrumpPlayers = [CardPlayer]()
////for name in names {
////    players.append(TrumpPlayers(withName: name))
////}
////
////var newGameTrump = FoolTrumpGame(with: Deck(of: .stripped36))
////for var player in TrumpPlayers {
////    newGameTrump.add(player: &player)
////}
////newGameTrump.play()
////
////if newGame.players.count == 1 {
////    print(newGame.players[0].name + " в дураках!")
////} else {
////    print("Игра завершилась вничью!")
////}

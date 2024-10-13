type Domino = (u8, u8);

fn rev(d: Domino) -> Domino {
    (d.1, d.0)
}

pub fn chain(input: &[(u8, u8)]) -> Option<Vec<(u8, u8)>> {
    let ln = input.len();
    if ln == 0 {
        return Some(vec![]);
    }
    for (i, x) in input.iter().enumerate() {
        let mut mask = (1<<ln)-1;
        mask = mask ^ (1 << i);
        let mut chain:Vec<Domino> = vec![x.to_owned()];
        if let Some(y) = backtrack(input, mask, &mut chain) {
            return Some(y);
        }
    }
    None
}

fn backtrack(dominos: &[Domino], mask: u16, chain: &mut Vec<Domino>) -> Option<Vec<Domino>> {
    if mask == 0 {
        if chain.first().unwrap().0 != chain.last().unwrap().1 {
            return None;
        }
        return Some(chain.to_vec());
    }

    for i in 0..dominos.len() {
        if mask & (1 << i) == 0 {
            continue;
        }
        let cur = dominos[i];
        for cur in [cur, rev(cur)].iter().cloned() {
            if chain.last().unwrap().1 == cur.0 {
                chain.push(cur);
                if let Some(nc) = backtrack(dominos, mask ^ (1<<i), chain) {
                    return Some(nc);
                }
                chain.pop();
            }
        }
    }
    None
}
